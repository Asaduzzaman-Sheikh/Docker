from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(PAGE_TEMPLATE)

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form.get('username', '').strip()
    if not user_input:
        return render_template_string(PAGE_TEMPLATE, error='Please enter your name.')

    return render_template_string(PAGE_TEMPLATE, username=user_input)


PAGE_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#08111f">
    <title>Container Hello | Docker Demo</title>
    <style>
        :root {
            color-scheme: dark;
            --ink: #edf4ff;
            --muted: #91a2ba;
            --line: rgba(167, 193, 230, .16);
            --panel: rgba(11, 25, 45, .7);
            --accent: #6ee7c8;
            --accent-strong: #32c7a2;
        }

        * { box-sizing: border-box; }

        body {
            min-height: 100vh;
            margin: 0;
            overflow-x: hidden;
            background: #08111f;
            color: var(--ink);
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
                "Segoe UI", sans-serif;
        }

        body::before,
        body::after {
            position: fixed;
            z-index: -1;
            width: 34rem;
            height: 34rem;
            border-radius: 50%;
            content: "";
            filter: blur(80px);
            opacity: .16;
        }

        body::before { top: -13rem; left: -10rem; background: #1d7cf2; }
        body::after { right: -14rem; bottom: -16rem; background: #1cc99a; }

        .shell {
            display: grid;
            min-height: 100vh;
            place-items: center;
            padding: 2rem 1.25rem;
        }

        .card {
            width: min(100%, 980px);
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 30px;
            background: var(--panel);
            box-shadow: 0 30px 100px rgba(0, 0, 0, .35);
            backdrop-filter: blur(24px);
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1.5rem 1.75rem;
            border-bottom: 1px solid var(--line);
        }

        .brand { display: flex; align-items: center; gap: .75rem; font-weight: 700; }
        .brand-mark {
            display: grid;
            width: 2.25rem;
            height: 2.25rem;
            place-items: center;
            border-radius: 11px;
            color: #06121e;
            background: linear-gradient(135deg, var(--accent), #b9ffe9);
            box-shadow: 0 8px 25px rgba(110, 231, 200, .22);
        }

        .status {
            display: inline-flex;
            align-items: center;
            gap: .5rem;
            color: var(--muted);
            font-size: .78rem;
            letter-spacing: .04em;
            text-transform: uppercase;
        }

        .status::before {
            width: .5rem;
            height: .5rem;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 14px var(--accent);
            content: "";
        }

        .content {
            display: grid;
            grid-template-columns: 1.05fr .95fr;
            gap: clamp(2rem, 6vw, 5rem);
            padding: clamp(2.5rem, 7vw, 5.75rem);
        }

        .eyebrow {
            margin: 0 0 1.15rem;
            color: var(--accent);
            font-size: .75rem;
            font-weight: 700;
            letter-spacing: .16em;
            text-transform: uppercase;
        }

        h1 {
            max-width: 13ch;
            margin: 0;
            font-size: clamp(2.8rem, 7vw, 5.5rem);
            line-height: .96;
            letter-spacing: -.07em;
        }

        .intro {
            max-width: 35rem;
            margin: 1.75rem 0 0;
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.7;
        }

        .form-panel {
            align-self: center;
            padding: clamp(1.35rem, 3vw, 2rem);
            border: 1px solid var(--line);
            border-radius: 22px;
            background: rgba(4, 13, 27, .45);
        }

        label {
            display: block;
            margin-bottom: .7rem;
            color: #cbd7e8;
            font-size: .86rem;
            font-weight: 650;
        }

        .input-wrap { position: relative; }

        input {
            width: 100%;
            padding: 1rem 1.1rem;
            border: 1px solid rgba(167, 193, 230, .24);
            border-radius: 12px;
            outline: none;
            color: var(--ink);
            background: rgba(8, 17, 31, .75);
            font: inherit;
            transition: border-color .2s, box-shadow .2s;
        }

        input::placeholder { color: #5f7089; }
        input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 4px rgba(110, 231, 200, .12);
        }

        button {
            width: 100%;
            margin-top: .9rem;
            padding: 1rem 1.2rem;
            border: 0;
            border-radius: 12px;
            cursor: pointer;
            color: #06121e;
            background: linear-gradient(135deg, var(--accent), #a7ffe5);
            font: inherit;
            font-weight: 800;
            transition: transform .2s, box-shadow .2s;
        }

        button:hover { transform: translateY(-2px); box-shadow: 0 12px 25px rgba(110, 231, 200, .2); }
        button:focus-visible { outline: 3px solid #fff; outline-offset: 3px; }

        .message {
            margin: 1.2rem 0 0;
            padding: .9rem 1rem;
            border-radius: 12px;
            color: #b8ffec;
            background: rgba(50, 199, 162, .1);
            line-height: 1.5;
        }

        .error { color: #ffc0c0; background: rgba(255, 104, 104, .1); }

        .footer {
            padding: 1.2rem 1.75rem;
            border-top: 1px solid var(--line);
            color: #687b95;
            font-size: .78rem;
            text-align: center;
        }

        @media (max-width: 720px) {
            .topbar { padding: 1.1rem 1.25rem; }
            .status { display: none; }
            .content { grid-template-columns: 1fr; padding: 3rem 1.5rem; }
            h1 { max-width: 10ch; }
        }
    </style>
</head>
<body>
    <main class="shell">
        <section class="card" aria-labelledby="page-title">
            <header class="topbar">
                <div class="brand">
                    <span class="brand-mark" aria-hidden="true">◈</span>
                    <span>Container Hello</span>
                </div>
                <span class="status">Live container</span>
            </header>
            <div class="content">
                <div>
                    <p class="eyebrow">A tiny Docker experience</p>
                    <h1>Say hello to your container.</h1>
                    <p class="intro">
                        A clean, friendly way to see your Flask app come alive.
                        Enter your name and let this little service welcome you.
                    </p>
                </div>
                <div class="form-panel">
                    <form action="/greet" method="post">
                        <label for="username">What should we call you?</label>
                        <div class="input-wrap">
                            <input id="username" name="username" type="text"
                                placeholder="Your name" autocomplete="name" required autofocus>
                        </div>
                        <button type="submit">Create my welcome <span aria-hidden="true">→</span></button>
                    </form>
                    {% if username %}
                        <p class="message" role="status">Hello {{ username }}, welcome to this Docker demo.</p>
                    {% elif error %}
                        <p class="message error" role="alert">{{ error }}</p>
                    {% endif %}
                </div>
            </div>
            <footer class="footer">Built with Flask · Running wherever containers run</footer>
        </section>
    </main>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)