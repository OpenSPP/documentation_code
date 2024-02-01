import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080/',
  realm: 'OpenSPP',
  clientId:'user-portal',
  redirectUri: "http://localhost:3000", // local development redirect uri
});

export default keycloak;