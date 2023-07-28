<template>
    <div class="super-admin-template">
      <header>
        <!-- Barre de navigation avec les paramètres utilisateurs -->
        <nav class="user-navigation">
          <!-- Paramètres utilisateurs -->
          <ul>
          <li><a href="#">Paramètre 1</a></li>
          <li><a href="#">Paramètre 2</a></li>
          <li><a href="#">Paramètre 3</a></li>
        </ul>
        </nav>
      </header>
      
      <aside>
        <!-- Barre latérale avec les éléments de navigation -->
        <nav class="sidebar-navigation">
          <ul>
            <li><a href="#hospitals">Hôpitaux</a></li>
            <li><a href="#administration">Administration</a></li>
            <li><a href="#subscriptions">Abonnements</a></li>
            <li><a href="#messages">Messages</a></li>
            <li><a href="#logs">Journaux</a></li>
          </ul>
        </nav>
      </aside>
      
      <main>
        <section class="page-title">
          <!-- Affichage du titre, du slogan et du fil d'Ariane de la page actuelle -->
          <h1>Super Admin Dashboard</h1>
          <p>Slogan de la page actuelle</p>
          <nav class="breadcrumb">
            <!-- Fil d'Ariane -->
            <ul>
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Section 1</a></li>
            <li><a href="#">Section 2</a></li>
            <li>Page actuelle</li>
          </ul>
          </nav>
        </section>
        
        <section class="widget-cards">
          <!-- Zone de contenu principale avec des cartes de widget -->
          <div class="widget-card">
          <h2>Widget 1</h2>
          <p>Contenu du premier widget</p>
        </div>
        <div class="widget-card">
          <h2>Widget 2</h2>
          <p>Contenu du deuxième widget</p>
        </div>
          <!-- Ajoutez plus de cartes de widget ici -->
        </section>
      </main>
      
      <footer>
        <p>Copyright &copy;2023 All rights reserved | ITTS</p>
      </footer>
    </div>
</template>
  
  <script>
  export default {
    name: 'SuperAdmin',
    // Composants enfants
  }
  </script>
  
  <style  lang="scss" scoped></style>
  