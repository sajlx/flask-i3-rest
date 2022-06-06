# flask-i3-rest-base

-----------------------

## get multiple objects if possible it's better if methods are lazy
```
get_all_objs(**kwargs)
filter_all_objs(all_objs, **kwargs)

paginate_obj(filtered_multiple_objs, **kwargs)
```
## get single object after `get_all_objs` and `filter_all_objs`
```
get_single_obj(filtered_multiple_objs, **kwargs)
```

## serialize for output single and multiple objects for pass to `flask jsonify`
```
serialize_many(paginated_filtered_multiple_objs, **kwargs)
serialize_single_obj(single_obj, **kwargs)
```

## validate input for create/update single or multiple objects
```
validate_create_input(**kwargs)
validate_update_input(**kwargs)
```

## perform true operation for create update and delete
```
perform_create(validated_data, **kwargs)
perform_update(single_obj, validated_data, **kwargs)
perform_partial_update(single_obj, validated_data, **kwargs)
perform_delete(single_obj, validated_data, **kwargs)
```