"""Override the underlying HTML template."""

app_layout = '''<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body>
            <nav>
                <a href="/"><i class="fas fa-home"></i> Home</a>
                <a href="/commands/"><i class="fas fa-list"></i> Commands</a>
                <a href="/database/"><i class="fas fa-database"></i> Database</a>
                <a href="/users/"><i class="fas fa-user-friends"></i> Users</a>
            </nav>
            <div class="layout-container">
                <div class="filter">
                    <span>Filter by type:</span>
                    <button id="avi-filter">avi</button>
                    <button id="basic-filter">basic</button>
                    <button id="crypto-filter">crypto</button>
                    <button id="goal-filter">goal</button>
                    <button id="random-filter">random</button>
                    <button id="etc-filter">etc</button>
                </div>
                {%app_entry%}
            </div>
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>'''
