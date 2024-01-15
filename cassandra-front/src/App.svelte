<script>
  import parspooyeshLogo from './assets/parspooyesh_logo.jpeg'

  import Counter from './lib/Counter.svelte'
  import Form from './lib/Form.svelte'
</script>

<main>
  <div>
    <a href="http://www.parspooyesh.com/" target="_blank" rel="noreferrer">
      <img src={parspooyeshLogo} class="logo" alt="Parspooyesh Logo" />
    </a>
  </div>
  <h1>Parspooyesh AI</h1>

  <Form />

</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #ff0000aa);
  }

</style>
