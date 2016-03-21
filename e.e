HTTP/1.1 403 FORBIDDEN
Server: gunicorn/17.5
Date: Mon, 21 Mar 2016 15:28:47 GMT
Connection: close
Transfer-Encoding: chunked
X-Frame-Options: SAMEORIGIN
Content-Type: text/html


<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>403 Forbidden</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background:#eee; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 span { font-size:60%; color:#666; font-weight:normal; }
    #info { background:#f6f6f6; }
    #info ul { margin: 0.5em 4em; }
    #info p, #summary p { padding-top:10px; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
  </style>
</head>
<body>
<div id="summary">
  <h1>Forbidden <span>(403)</span></h1>
  <p>CSRF verification failed. Request aborted.</p>

</div>

<div id="info">
  <h2>Help</h2>
    
    <p>Reason given for failure:</p>
    <pre>
    CSRF cookie not set.
    </pre>
    

  <p>In general, this can occur when there is a genuine Cross Site Request Forgery, or when
  <a
  href='http://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ref-contrib-csrf'>Django's
  CSRF mechanism</a> has not been used correctly.  For POST forms, you need to
  ensure:</p>

  <ul>
    <li>Your browser is accepting cookies.</li>

    <li>The view function uses <a
    href='http://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext'><code>RequestContext</code></a>
    for the template, instead of <code>Context</code>.</li>

    <li>In the template, there is a <code>{% csrf_token
    %}</code> template tag inside each POST form that
    targets an internal URL.</li>

    <li>If you are not using <code>CsrfViewMiddleware</code>, then you must use
    <code>csrf_protect</code> on any views that use the <code>csrf_token</code>
    template tag, as well as those that accept the POST data.</li>

  </ul>

  <p>You're seeing the help section of this page because you have <code>DEBUG =
  True</code> in your Django settings file. Change that to <code>False</code>,
  and only the initial error message will be displayed.  </p>

  <p>You can customize this page using the CSRF_FAILURE_VIEW setting.</p>
</div>

</body>
</html>
