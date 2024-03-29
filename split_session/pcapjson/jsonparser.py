import json
import sys

def parse(target:str, on_parse, on_error, *, unhandle_error=False):
    sys.stderr.write("\n")

    with open(target, 'r', encoding='utf-8') as f:
        json_object = json.load(f)

    for i, data in enumerate(json_object):
        try:
            on_parse(data=data)
        except KeyError as ex:
            if unhandle_error:
                raise
            else:
                val = data['_source']['layers']['frame']['frame.time_relative']

                sys.stderr.write(f'Exception Occurs : KeyError ')
                sys.stderr.write(f"{ex}")
                sys.stderr.write(f'\n')
                on_error(data=data, exception=ex, number = i+1)
        except Exception as ex:
            if unhandle_error:
                raise
            else:
                on_error(data=data, exception=ex, number = i+1)

        