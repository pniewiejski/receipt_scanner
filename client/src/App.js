import React, { Component } from 'react';
import './App.css';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import Home from './components/Home';

const theme = createMuiTheme({
  typography: {
    useNextVariants: true,
  },
  palette: {
    primary: {
      light: '#a4a4a4',
      main: '#757575',
      dark: '#4caf50',
      contrastText: '#ffffff',
    },
    secondary: {
      light: '#8e8e8e',
      main: '#8e8e8e',
      dark: '#616161',
      contrastText: '#ffffff',
    },
  },
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <div className="App">
      <Home />
      </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
