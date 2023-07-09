from rest_framework.renderers import JSONRenderer
import json

class UserRenderer(JSONRenderer):
  charset='utf-8'
  def render(self, data, accepted_media_type=None, renderer_context=None):
    json_data = ''
    if 'ErrorDetail' in str(data):
      json_data = json.dumps({'error':data})
    else:
      json_data = json.dumps(data)
    
    return json_data