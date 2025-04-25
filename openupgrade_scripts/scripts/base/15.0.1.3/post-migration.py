# Copyright 2021 Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


def full_module_dependencies(env, modules):
    dependencies = env["ir.module.module"]
    if modules.dependencies_id:
        dependencies = env["ir.module.module"].search(
            [("name", "in", modules.dependencies_id.mapped("name"))]
        )
        if dependencies:
            dependencies |= full_module_dependencies(env, dependencies)
    return dependencies


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "base", "15.0.1.3/noupdate_changes.xml")
