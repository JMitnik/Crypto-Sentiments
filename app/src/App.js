import React, { Component } from 'react';
import ReactDom from 'react-dom';
import logo from './logo.svg';
import TweetOverview from './TweetOverview';
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
        <TweetOverview></TweetOverview>
      </div>
    );
  }
}

export default App;
