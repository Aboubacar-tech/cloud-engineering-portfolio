fields @timestamp, @message
| filter @message like /Slow response/
| sort @timestamp desc