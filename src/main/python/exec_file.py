#coding=utf-8
"""This is the general module that allow ArcGIS Runtime to execute an abitrary script. In this case we just need the script be executed. We don't care its results.
So we call it "execute a script"
"""

import subprocess
import StringIO
import gzip

# By any menas, we first import. This is a workaround to prevent ArcGIS Desktop detect imports when creating the gpk
arc = __import__("arcpy")
#import arcpy
arc.env.overwriteOutput = True
arc.env.workspace = "in_memory"


def decode_global_vars(global_vars):
    """
    :param global_vars: str the
    :return a dictionary of global variables and their values could be fed to the script body
    :rtype dict
    """
    var_list = global_vars.split(';')
    var_dict = {}
    for var_str in var_list:
        var_name, var_value_tuple = var_str.split('<-')
        ispath, encode, var_value_encoded = var_value_tuple.split('|')
        if encode.find('b64') != -1:
            var_value_encoded = var_value_encoded.decode('base64').replace('\n', '')
        if encode.find('zlib') != -1:
            r = StringIO.StringIO(var_value_encoded)
            s = gzip.GzipFile(fileobj=r)
            var_value_encoded = s.read()
        var_value = var_value_encoded.replace('\n', '')
        if ispath.lower() == 'path':
            try:
                proc = subprocess.Popen(["winepath", "-w", var_value], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = proc.communicate()
                status = proc.returncode
                arc.AddMessage(output)
                if status == 0:
                    var_value = output
                    arc.AddMessage('the decoded path points -> %s' % var_value)
                else:
                    arc.AddWarning(output)
                    arc.AddWarning(err)
            except OSError, ex:
                arc.AddWarning(str(ex))
        var_dict[var_name] = var_value
    return var_dict

global_vars = arc.GetParameterAsText(0)
script_body = arc.GetParameterAsText(1)

for k, v in decode_global_vars(global_vars).iteritems():
    arc.AddMessage("Add %s=%s to global variables" % (k, v))
    globals()[k] = v

script_ast = compile(script_body.decode('string_escape'), "<script>", "exec")

exec script_ast in globals()



