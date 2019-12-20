# /src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BlogpostModel import BlogpostModel, BlogpostSchema

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogpostSchema()


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
  Create Blogpost Function
  """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = blogpost_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    post = BlogpostModel(data)
    post.save()
    data = blogpost_schema.dump(post).data
    return custom_response(data, 201)


def custom_response(res, status_code):
    """
  Custom Response Function
  """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
