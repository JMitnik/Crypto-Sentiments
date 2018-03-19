import React, { Component } from 'react';
import logo from './logo.svg';
import DataBoard from './Databoard';
import './App.css';
import './_main.scss';

class App extends Component {
  render() {
    return (
      <div className="App container-fluid">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <DataBoard></DataBoard>
      </div>
    );
  }
}

export default App;
