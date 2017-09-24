import React from 'react';
import SimpleCounter from './SimpleCounter';

export default class HelloWorld extends React.Component {





  constructor() {
    console.log("in constructor")
  super();
  this.test1 = 'hello this is a test';
  this.state = {images: [ {url: <img src = "https://media.tenor.com/images/2d9c929afc278956a05b68d9bd9f2367/tenor.gif"/>, duration: 3000},
              {url: <img src = "https://media.tenor.com/images/51302798cf651e8196578b362136ce86/tenor.gif"/>, duration: 1000},
              {url: <img src = "https://media.giphy.com/media/eGFxvzNDoaGKA/giphy.gif"/>, duration: 2000},
              {url: <img src = "https://s3.amazonaws.com/blog.invisionapp.com/uploads/2017/04/gif-09.gif"/>, duration: 2000},
              {url: <img src = "https://img.buzzfeed.com/buzzfeed-static/static/2014-07/18/10/enhanced/webdr09/anigif_enhanced-buzz-22799-1405693809-7.gif?downsize=715:*&output-format=auto&output-quality=auto"/>
              , duration: 3000}
              ],

        idx: 0}
  this.changeImage()
  }
  // changeTest () {
  //       this.setState({
  //         test2:'hey man'
  //       });
  // }

  changeImage() {
          console.log('In change image');
          var imageIndex=0;
          var x = this;
          function change () {
              x.setState({idx: imageIndex});
              imageIndex++;
              if (imageIndex>=x.state.images.length) {
                  imageIndex=0;
              }
              console.log("called");
              setTimeout(change, x.state.images[imageIndex]["duration"])
          }
          change(x)
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div>
        <p>Music Gif</p>
        {/*<iframe src="https://giphy.com/embed/3o85xGocUH8RYoDKKs" width="480" height="268" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        {this.test1}
        <br/>
        {this.state.test2}
        this.images[0]
        <SimpleCounter />*/}
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
        {this.state.images[this.state.idx]["url"]}

        {/*<button onClick={this.changeImage.bind(this)} >Click Me!</button>*/}
      </div>
    );
  }
}
