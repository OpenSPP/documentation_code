import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import keycloak from './keycloak';
const root = ReactDOM.createRoot(document.getElementById('root'));

keycloak.init({
  onLoad: 'check-sso'
}).then((auth)=>{
  if(auth){
    console.log(auth)
    console.log("User is logged in");
  }
  else {
    console.log('User is not logged in');
  }
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
  
}).catch((error)=>{
  console.error('Keycloak failed:',error);
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
