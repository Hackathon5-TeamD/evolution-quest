def app(env, start_response): #2つの引数を持つ関数
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, response_headers) #ステータスコードとレスポンスヘッダをセット

    if env.get("PATH_INFO") == "/": # "/" パス
        return [b'Hello World\n'] #バイト列を返す
    if env.get("PATH_INFO") == "/other": # "/other" パス
        return [b'Other World\n'] #バイト列を返す
