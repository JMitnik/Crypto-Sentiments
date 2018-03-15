import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import List from './List';

const TWEET_URL = `http://127.0.0.1:5000/tweets`;

class TweetOverview extends Component {
    state = {
        tweets: {}
    }

    fetchTweets = (event) => {
        event.preventDefault();
        console.log(event);

        fetch(TWEET_URL)
        .then(res => res.json())
        .then(data => this.setState({tweets: data}));
    }

    render() {
        return (
            <div>
                <div>
                    <button onClick={e => this.fetchTweets(e)}></button>
                </div>
                <List items={this.state.tweets}>

                </List>
            </div>
        )
    }
 }

export default TweetOverview;
