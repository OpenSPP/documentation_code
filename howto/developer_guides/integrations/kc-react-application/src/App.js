import './App.css';
import keycloak from './keycloak';
function App() {
  const login = () => {
    keycloak.login();
  }
  const logout = () =>{
    keycloak.logout();
  }
  return (
    <div className="App">
      <div>
      {keycloak.authenticated ? (
        <button onClick={logout}>Logout </button>
      ) : (
        <button onClick={login}>Login </button>
        ) 
      }
      </div>
    </div>
  );
}

export default App;
