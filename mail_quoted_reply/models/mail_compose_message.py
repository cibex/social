from markupsafe import Markup

from odoo import api, fields, models, tools


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    is_reply_readonly = fields.Boolean(default=True)
    reply_body = fields.Html(default='')
    is_separate_body = fields.Boolean(compute='_compute_is_separate_body')

    @api.onchange("template_id")
    def _onchange_template_id_wrapper(self):
        super()._onchange_template_id_wrapper()
        context = self._context
        if "is_quoted_reply" in context.keys() and context["is_quoted_reply"]:
            if self.is_separate_body:
                self.reply_body = context["quote_body"]
            else:
                self.body += Markup(context["quote_body"])
        return

    @api.onchange('is_reply_readonly')
    def _onchange_is_reply_readonly(self):
        if self.reply_body:
            self.reply_body = Markup(self.reply_body)

    @api.depends('reply_body')
    def _compute_is_separate_body(self):
        parameter_string = self.env['ir.config_parameter'].sudo().get_param('mail_quoted_reply.separate_reply_body', '')
        self.is_separate_body = parameter_string.lower() not in ['', 'false', '0']

    def get_mail_values(self, res_ids):
        results = super(MailComposeMessage, self).get_mail_values(res_ids)
        if self.is_separate_body and self.reply_body:
            for res_id in res_ids:
                values = results.get(res_id)
                reply_body = Markup(self.reply_body)
                values.update({'body': values.get('body') + reply_body})
        return results

    @api.model
    def get_record_data(self, values):
        result = super().get_record_data(values)
        subj = self._context.get("default_subject", False)
        if subj:
            result["subject"] = tools.ustr(subj)
        return result
