<script>
let visible = false;
let message = '';
let ai_response = '';

async function sendMsgToAPI() {
    visible = false;
    try {
        const response = await fetch('http://172.17.102.130:6969/api/message', {
            method: 'POST',
            headers: {
                "Access-Control-Allow-Origin": "http://172.17.102.130:6969/api/message",
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'msg': message
            })
        });
        if (!response.ok) throw new Error(`HTTP error!!! status: ${response.status}`);
        const result = await response.json(); // wait for the promise to resolve and get JSON result
        ai_response = result['msg'];
        visible = true;
    } catch (error) {
        console.log('There was a problem with posting the data: ', error);
    };
};

function typewriter(node, { speed = 5 }) {
		const valid = node.childNodes.length === 1 && node.childNodes[0].nodeType === Node.TEXT_NODE;

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length / (speed * 0.01);

		return {
			duration,
			tick: (t) => {
				const i = ~~(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	};
</script>

<input bind:value={message} type="input" class="form__field" placeholder="Question" name="name" id='name' />
<button on:click={sendMsgToAPI}>Ask!</button>

{#if visible}
<p transition:typewriter>{ai_response}</p>
{/if}

<style lang="scss">
$primary: #991111;
$secondary: #ef8138;
$white: #213547;
$gray: #9b9b9b;
.form__group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
  width: 50%;
}

.form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid $gray;
  outline: 0;
  font-size: 1.3rem;
  color: $white;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;

  &::placeholder {
    color: transparent;
  }

  &:placeholder-shown ~ .form__label {
    font-size: 1.3rem;
    cursor: text;
    top: 20px;
  }
}

.form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: $gray;
}

.form__field:focus {
  ~ .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 1rem;
    color: $primary;
    font-weight:700;    
  }
  padding-bottom: 6px;  
  font-weight: 700;
  border-width: 3px;
  border-image: linear-gradient(to right, $primary,$secondary);
  border-image-slice: 1;
}
.form__field{
  &:required,&:invalid { box-shadow:none; }
}
body {
  font-family: 'Poppins', sans-serif; 
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  background-color:#222222;
}
</style>