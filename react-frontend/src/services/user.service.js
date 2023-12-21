export function getUser() {
    const token = getToken();
    return token ? JSON.parse(atob(token.split('.')[1])).user : null;
  }

  export function getToken() {
    let token = localStorage.getItem('token');
    console.log('TOKEN IN getToken;', token)
    if (!token) return null;
    // Check if expired, remove if it is
    const payload = JSON.parse(atob(token.split('.')[1]));
    // JWT's exp is expressed in seconds, not milliseconds, so convert
    if (payload.exp < Date.now() / 1000) {
      localStorage.removeItem('token');
      return null;
    }
    return token;
  }