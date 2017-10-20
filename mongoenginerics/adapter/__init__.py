from . import apistar as _as

ADAPTER_MAP = {
    'apistar': _as.ApiStarAdapter
}


def run(app):
    engine_name = get_adapter_name(app.engine)
    adapter = ADAPTER_MAP[engine_name](app)

    print(adapter._handles)
    print(adapter.engine)

    for controller in app._controllers:
        ctrl = controller()
        adapter.attach(ctrl)

    adapter.mount_app()
    return adapter.run()


def get_adapter_name(engine):
    return 'apistar'