import React, {Component} from "react";
import {BrowserRouter, Switch, Route, Link, Redirect} from "react-router-dom";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path={"/"}><p>This is Home Page</p></Route>
                    <Route path={"/join"} component={RoomJoinPage}/>
                    <Route path={'/create'} component={CreateRoomPage}/>
                </Switch>
            </BrowserRouter>
        );
    }

}