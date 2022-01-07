

def add_route(app_or_blueprint, view, path, name):

    _view = view.as_view(name)

    path_ends_with_slash = path.endswith('/')

    ensured_slash_end_path = "{}{}".format(
        path,
        "" if path_ends_with_slash else "/"
    )

    if hasattr(view, 'list'):
        app_or_blueprint.add_url_rule(
            ensured_slash_end_path,
            defaults={view.lookup: None},
            view_func=_view,
            methods=['GET']
        )

    if hasattr(view, 'create'):
        app_or_blueprint.add_url_rule(
            ensured_slash_end_path,
            defaults={view.lookup: None},
            view_func=_view,
            methods=['POST']
        )

    if (
        hasattr(view, 'retrieve')
        or hasattr(view, 'update')
        or hasattr(view, 'partial_update')
        or hasattr(view, 'destroy')
    ):

        single_element_path = '{}<{}:{}>/'.format(
            ensured_slash_end_path,
            view.lookup_kind,
            view.lookup
        )

        if hasattr(view, 'retrieve'):
            app_or_blueprint.add_url_rule(
                single_element_path,
                view_func=_view,
                methods=['GET']
            )
        if hasattr(view, 'update'):
            app_or_blueprint.add_url_rule(
                single_element_path,
                view_func=_view,
                methods=['POST']
            )
        if hasattr(view, 'partial_update'):
            app_or_blueprint.add_url_rule(
                single_element_path,
                view_func=_view,
                methods=['PATCH']
            )
        if hasattr(view, 'destroy'):
            app_or_blueprint.add_url_rule(
                single_element_path,
                view_func=_view,
                methods=['DELETE']
            )
