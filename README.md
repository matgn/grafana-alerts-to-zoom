# Grafana Alerts To Zoom
> Just a little project written in Python to link Grafana Alerting (Webhook) with Zoom Incoming Webhook

## Getting started

You need to add the app Incoming Webook : https://marketplace.zoom.us/apps/eH_dLuquRd-VYcOsNGy-hQ
Once it's installed on your Workplace, create a channel and send the connection command.
```
/inc connect grafana
```
You'll receive a message with the Endpoint URL and Verification Token.

Now, you can setup the grafana-alerts-to-zoom translator.

With Docker :

```shell
docker run --rm -it -p <TCPPortYouWant>:<TCPPortYouWant> --env ZOOMENDPOINT="https://integrations.zoom.us/chat/webhooks/incomingwebhook/<YourURLPATH>" --env ZOOMTOKEN="<YourToken>" --env APPPORT=<TCPPortYouWant> --name grafana-alerts-to-zoom matgn/grafana-alerts-to-zoom:latest
# docker run --rm -it -p 5000:5000 --env ZOOMENDPOINT="https://integrations.zoom.us/chat/webhooks/incomingwebhook/df92-kj294-kfkirfc" --env ZOOMTOKEN="d932fks9203kdfkgs" --env APPPORT=5000 --name grafana-alerts-to-zoom matgn/grafana-alerts-to-zoom:latest
```

With Shell :
```shell
pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
export ZOOMENDPOINT="https://integrations.zoom.us/chat/webhooks/incomingwebhook/<YourURLPATH>"
export ZOOMTOKEN="<YourToken>"
gunicorn application:app -b 0.0.0.0:<TCPPortYouWant>
#gunicorn application:app -b 0.0.0.0:5000
```

Finally, you can configure Grafana to set the Grafana Webhook (Alerting -> Contact Points -> Add)
```
Integration : WebHook
URL : <http://YourDomainOrIPAddress:Port/requests>
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
