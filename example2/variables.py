str="""    <div id="heading">
       <h1 id="paste">Edit the data</h1>
	<nav id="navi">
	<a id="about" href="/">About</a>

	</nav>
   </div>
      <form action = "http://localhost:5000/login" method = "post">
	<div id="lex">
	<p class="options-lexer">
      <select name="lexer" id="id_lexer">
        <optgroup label="Text">
            <option value="text">Plain Text</option>
            <option value="rst">reStructuredText</option>
        </optgroup>
        <optgroup label="Code">
            <option value="text">Plain Code</option>
            <option value="applescript">AppleScript</option>
            <option value="arduino">Arduino</option>
            <option value="bash">Bash</option>
            <option value="bat">Batchfile</option>
            <option value="c">C</option>
            <option value="clojure">Clojure</option>
            <option value="cmake">CMake</option>
            <option value="coffee-script">CoffeeScript</option>
            <option value="common-lisp">Common Lisp</option>
            <option value="console">Console/Bash Session</option>
            <option value="csharp">C#</option>
            <option value="css">CSS</option>
            <option value="cuda">CUDA</option>
            <option value="dart">Dart</option>
            <option value="delphi">Delphi</option>
            <option value="diff">Diff</option>
            <option value="django">Django/Jinja</option>
            <option value="docker">Docker</option>
            <option value="elixir">Elixir</option>
            <option value="erlang">Erlang</option>
            <option value="go">Go</option>
            <option value="handlebars">Handlebars</option>
            <option value="haskell">Haskell</option>
            <option value="html">HTML</option>
            <option value="html+django">HTML + Django/Jinja</option>
            <option value="ini">INI</option>
            <option value="irc">IRC logs</option>
            <option value="java" >Java</option>
            <option value="js">JavaScript</option>
            <option value="kotlin">Kotlin</option>
            <option value="less">LessCSS</option>
            <option value="lua">Lua</option>
            <option value="make">Makefile</option>
            <option value="matlab">Matlab</option>
            <option value="nginx">Nginx configuration file</option>
            <option value="numpy">NumPy</option>
            <option value="objective-c">Objective-C</option>
            <option value="perl">Perl</option>
            <option value="php">PHP</option>
            <option value="postgresql">PostgreSQL SQL dialect</option>
            <option value="python" selected="">Python</option>
            <option value="rb">Ruby</option>
            <option value="rust">Rust</option>
            <option value="sass">Sass</option>
            <option value="scss">SCSS</option>
            <option value="sql">SQL</option>
            <option value="swift">Swift</option>
            <option value="tex">TeX</option>
            <option value="typoscript">TypoScript</option>
            <option value="vim">VimL</option>
            <option value="xml">XML</option>
            <option value="xslt">XSLT</option>
            <option value="yaml">YAML</option>
        </optgroup>
        </select>
        </p>
          <p class="options-expire">
              <select name="expires" id="id_expires">
              <option value="0">One Time Snippet</option>
              <option value="3600">Expire in 1 hour</option>
              <option value="86400">Expire in 24 hours</option>
              <option value="604800" selected="">Expire in 7 days</option>
              </select>
           </p>
	<p><input id ="submit" type = "submit" value = "Paste" /></p>
	</div>
         <p><textarea rows="30" cols="215" name = "nm" placeholder="Enter the data here..........">
         """