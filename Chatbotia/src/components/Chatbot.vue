<template>
    <div class="chatbot">
      <h1>Chatbot</h1>
      <div class="chat-window">
        <div class="messages" v-for="(message, index) in messages" :key="index">
          <div class="user-message">{{ message.user }}</div>
          <div class="bot-response">{{ message.bot }}</div>
        </div>
      </div>
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Envoyer un message..." />
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        userInput: '',
        messages: []
      };
    },
    methods: {
      async sendMessage() {
        if (this.userInput.trim() === '') return
  
        const userMessage = this.userInput
        this.messages.push({ user: userMessage, bot: '' })
        this.userInput = ''
    
        const response = await this.fetchResponse(userMessage);
        this.messages[this.messages.length - 1].bot = response;
      },
      async fetchResponse(message) {
        try {
          const response = await axios.post('http://localhost:5000/chat', {
            content: message
          });
          return response.data.message.content
        } catch (error) {
          return 'Error fetching response'
        }
      }
    }
  };
</script>

<style scoped>
.chatbot {
    max-width: 90%;
    margin: auto;
    padding: 2%;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-family: 'Arial', sans-serif;
}

.chat-window {
    height: 60vh;
    overflow-y: auto;
    border: 1px solid #ddd;
    margin-bottom: 2%;
    padding: 2%;
    background-color: #fff;
    border-radius: 8px;
}

.messages {
    margin-bottom: 2%;
    display: flex;
    flex-direction: column;
}

.user-message {
    align-self: flex-end;
    background-color: #007bff;
    color: #fff;
    padding: 2%;
    border-radius: 15px;
    margin-bottom: 1%;
    max-width: 80%;
    word-wrap: break-word;
}

.bot-response {
    align-self: flex-start;
    background-color: #e9ecef;
    color: #333;
    padding: 2%;
    border-radius: 15px;
    margin-bottom: 1%;
    max-width: 80%;
    word-wrap: break-word;
}

input {
    width: 100%;
    padding: 2%;
    border: 1px solid #ccc;
    border-radius: 25px;
    box-sizing: border-box;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.3s;
}

input:focus {
    border-color: #007bff;
}

@media (max-width: 600px) {
    .chatbot {
        padding: 5%;
    }
    .chat-window {
        height: 80vh;
    }
    input {
        padding: 3%;
        font-size: 0.875rem;
    }
}
</style>