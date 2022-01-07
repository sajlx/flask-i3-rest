

import logging

from flask import abort
from flask import jsonify
# from flask import request
from flask.views import MethodView



from .exceptions import NotValidDeleteException


logger = logging.getLogger('i3-flask-rest')


class GenericModelResource(MethodView):

    lookup = "id"
    lookup_kind = "int"

    def _abort_no_method(self, method):
        if not getattr(self, method):
            abort(405)

    def get(self, **kwargs):
        if self.lookup in kwargs and kwargs.get(self.lookup):
            self._abort_no_method('retrieve')
            return getattr(self, 'retrieve')(**kwargs)
        else:
            self._abort_no_method('list')
            return getattr(self, 'list')(**kwargs)

    def post(self, **kwargs):
        if self.lookup in kwargs and kwargs.get(self.lookup):
            self._abort_no_method('update')
            return getattr(self, 'update')(**kwargs)
        else:
            self._abort_no_method('create')
            return getattr(self, 'create')(**kwargs)

    def patch(self, **kwargs):
        if self.lookup in kwargs and kwargs.get(self.lookup):
            self._abort_no_method('partial_update')
            return getattr(self, 'partial_update')(**kwargs)
        else:
            abort(405)
            # self._abort_no_method('create')
            # return getattr(self, 'create')(**kwargs)

    def delete(self, **kwargs):
        if self.lookup in kwargs and kwargs.get(self.lookup):
            self._abort_no_method('destroy')
            return getattr(self, 'destroy')(**kwargs)
        else:
            raise NotValidDeleteException()



class ListMixin(object):

    def list(self, **kwargs):
        all_objs = self.get_all_objs(**kwargs)
        filtered_multiple_objs = self.filter_all_objs(all_objs, **kwargs)
        paginated_filtered_multiple_objs = self.paginate_obj(filtered_multiple_objs, **kwargs)
        serialized_paginated_filtered_multiple_objs = self.serialize_many(paginated_filtered_multiple_objs, **kwargs)

        return jsonify(
            serialized_paginated_filtered_multiple_objs
        )


class RetrieveMixin(object):

    def retrieve(self, **kwargs):
        all_objs = self.get_all_objs(**kwargs)
        filtered_multiple_objs = self.filter_all_objs(all_objs, **kwargs)
        single_obj = self.get_single_obj(filtered_multiple_objs, **kwargs)
        serialized_single_obj = self.serialize_single_obj(single_obj, **kwargs)
        return jsonify(serialized_single_obj)


class CreateMixin(object):

    def create(self, **kwargs):
        validated_data = self.validate_create_input(**kwargs)
        new_single_obj = self.perform_create(validated_data, **kwargs)
        serialized_new_single_obj = self.serialize_single_obj(new_single_obj, **kwargs)
        return jsonify(serialized_new_single_obj), 201


class UpdateMixin(object):

    def update(self, **kwargs):

        all_objs = self.get_all_objs(**kwargs)
        filtered_multiple_objs = self.filter_all_objs(all_objs, **kwargs)
        single_obj = self.get_single_obj(filtered_multiple_objs, **kwargs)

        validated_data = self.validate_update_input(**kwargs)
        updated_single_obj = self.perform_update(single_obj, validated_data, **kwargs)

        serialized_single_obj = self.serialize_single_obj(updated_single_obj, **kwargs)

        return jsonify(serialized_single_obj), 200


class PartialUpdateMixin(object):

    def partial_update(self, **kwargs):

        all_objs = self.get_all_objs(**kwargs)
        filtered_multiple_objs = self.filter_all_objs(all_objs, **kwargs)
        single_obj = self.get_single_obj(filtered_multiple_objs, **kwargs)

        validated_data = self.validate_update_input(**kwargs)
        updated_single_obj = self.perform_partial_update(single_obj, validated_data, **kwargs)

        serialized_single_obj = self.serialize_single_obj(updated_single_obj, **kwargs)

        return jsonify(serialized_single_obj), 200


class DeleteMixin(object):

    def destroy(self, **kwargs):

        all_objs = self.get_all_objs(**kwargs)
        filtered_multiple_objs = self.filter_all_objs(all_objs, **kwargs)
        single_obj = self.get_single_obj(filtered_multiple_objs, **kwargs)

        validated_data = self.validate_update_input(**kwargs)
        delete_response_dict = self.perform_delete(single_obj, validated_data, **kwargs)

        if delete_response_dict:
            return jsonify(delete_response_dict), 200
        else:
            return jsonify({}), 204


# class FilterSet(object):

#     model = None

#     allowed_filters = None

#     def get_model(self):
#         assert self.model, "Not have model setted"
#         return self.model

#     def parse_filters(self, filters):


class ReadOnlyModelResource(ListMixin, RetrieveMixin, GenericModelResource):
    pass


class ModelResource(CreateMixin, UpdateMixin, DeleteMixin, ReadOnlyModelResource):
    pass


class NoDeleteModelResource(ModelResource):

    def destroy(self, **kwargs):
        abort(405)
