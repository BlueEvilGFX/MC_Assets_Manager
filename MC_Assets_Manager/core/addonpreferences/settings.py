def draw_settings_tab(self, context):
    """
    draws <settings>
    """
    layout = self.layout
    box = layout.box()

    # loading settings
    row = box.row()
    row.prop(
        self.main_props,
        "load_all_during_startup",
        text = "loads addon completely during startup",
        )

    # auto addon updater -> theDuckCow!
    row = box.row()
    row.prop(
        self,
        "auto_check_update",
        text="checks automatically for addon updates")

    # auto dlc update checker
    row = box.row()
    row.prop(
        self.main_props,
        "auto_check_dlc",
        text="checks for DLC updates during startup "
        )

    # two UIs in the n panel
    row = box.row()
    row.prop(
        self.main_props,
        "two_dlc_ui_panels",
        text="displaying two DLC UIs in the n panel")

    # storage path
    row = box.row()
    row.prop(self.main_props, "storage_path")