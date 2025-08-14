from odoo import models


class MailComposeMessageInherit(models.TransientModel):
    _inherit = "mail.compose.message"

    def default_get(self, fields_list):
        vals = super(MailComposeMessageInherit, self).default_get(
            fields_list=fields_list
        )
        default_cc_partner_ids = self._context.get("default_cc_partner_ids", [])
        if default_cc_partner_ids:
            vals.update(partner_cc_ids=default_cc_partner_ids)
        return vals
