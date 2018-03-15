import React, { Component } from 'react';
import ListItem from './ListItem';

const List = (props) =>
    Object.keys(props.items).forEach(item => <ListItem item={item}></ListItem>);

export default List;
