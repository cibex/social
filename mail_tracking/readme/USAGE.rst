When user sends a message in mail_thread (chatter), for instance in partner
form, then an email tracking is created for each email notification. Then a
status icon will appear just right to name of notified partner.

These are all available status icons:

.. |sent| image:: ../static/src/img/sent.png
   :width: 10px

.. |delivered| image:: ../static/src/img/delivered.png
   :width: 15px

.. |opened| image:: ../static/src/img/opened.png
   :width: 15px

.. |error| image:: ../static/src/img/error.png
   :width: 10px

.. |waiting| image:: ../static/src/img/waiting.png
   :width: 10px

.. |unknown| image:: ../static/src/img/unknown.png
   :width: 10px

.. |cc| image:: ../static/src/img/cc.png
   :width: 10px

.. |noemail| image:: ../static/src/img/no_email.png
   :width: 10px

.. |anonuser| image:: ../static/src/img/anon_user.png
   :width: 10px

|unknown|  **Unknown**: No email tracking info available. Maybe this notified partner has 'Receive Inbox Notifications by Email' == 'Never'

|waiting|    **Waiting**: Waiting to be sent

|error|    **Error**: Error while sending

|sent|    **Sent**: Sent to SMTP server configured

|delivered|    **Delivered**: Delivered to final MX server

|opened|  **Opened**: Opened by partner

|cc|  **Cc**: It's a Carbon-Copy recipient. Can't know the status so is 'Unknown'

|noemail|  **No Email**: The partner doesn't have a defined email

|anonuser|  **No Partner**: The recipient doesn't have a defined partner


If you want to see all tracking emails and events you can go to

* Settings > Technical > Email > Tracking emails
* Settings > Technical > Email > Tracking events

When the message generates an 'error' status, it will apear on discuss 'Failed'
channel. Any view with chatter can show the failed messages
too.

* Discuss

  .. image:: ../static/img/failed_message_discuss.png

* Chatter

  .. image:: ../static/img/failed_message_widget.png

You can use "Failed sent messages" filter present in all views to show records
with messages in failed status and that needs an user action.

* Filter

  .. image:: ../static/img/failed_message_filter.png

As there can be scenarios where sending a tracking img in the email body is
not desired, there is a global system parameter
"mail_tracking.tracking_img_disabled" that can be set to True to remove
the tracking img from all outgoing emails. Note that the **Opened** status
will not be available in this case.
