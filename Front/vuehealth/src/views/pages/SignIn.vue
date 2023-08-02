<template>
<div class="layer"></div>
<main class="page-center">
  <article class="sign-up">
    <h1 class="sign-up__title">Welcome back!</h1>
    <p class="sign-up__subtitle">Sign in to your account to continue</p>
    <form class="sign-up-form form" @submit.prevent="handleSignIn">
      <label class="form-label-wrapper" for="username">
        <p class="form-label">Email</p>
        <input class="form-input" type="email" id="username" v-model="username" placeholder="Enter your email" required>
      </label>
      <label class="form-label-wrapper">
        <p class="form-label" for="password">Password</p>
        <input class="form-input" type="password" id="password" v-model="password" placeholder="Enter your password" required>
      </label>
      <a class="link-info forget-link" href="##">Forgot your password?</a>
      <label class="form-checkbox-wrapper">
        <input class="form-checkbox" type="checkbox" required>
        <span class="form-checkbox-label">Remember me next time</span>
      </label>
      <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
      </div>
      <button type="submit" class="form-btn primary-default-btn transparent-btn">Sign in</button>
    </form>
  </article>
</main>
</template>
  
  <script>
  import axios from 'axios';

  export default {
    name: 'SignIn',
    // Logique du formulaire de connexion
    // ...
    methods: {
    handleSignIn() {
      const userData = {
        username: this.username,
        password: this.password
      };

      // Faire une requête POST vers l'API d'authentification
      axios.post('http://127.0.0.1:8000/Backend/api_auth/login', userData)
        .then(response => {
          // Gérer la réponse de l'API après une connexion réussie
          console.log('Utilisateur connecté !', response.data);
          // Rediriger l'utilisateur vers une autre page si nécessaire
          this.$router.push('/HomePage.vue');
        })
        .catch(error => {
          // Gérer les erreurs d'authentification
          console.error('Échec de connexion', error.response.data.message);
          this.errorMessage = error.response.data.message;
        });
    }
  }
};
  </script>
  
  <style scoped>
  /* Styles spécifiques pour le formulaire de connexion */
  /* ... */
  </style>
  