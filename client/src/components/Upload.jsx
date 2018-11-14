import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import { withStyles }  from '@material-ui/core/styles';

const styles = theme => ({
    button: {
      margin: theme.spacing.unit,
    },
    rightIcon: {
      marginLeft: theme.spacing.unit,
    },
    input: {
        display: "none"
    }
  });

class Upload extends Component {
    
    constructor(props){
        super(props);

        this.uploadInput = React.createRef();

        this.state = {
            imageUrl: '',
        };

        this.handleImageUpload = this.handleImageUpload.bind(this);
    }

    handleImageUpload(event){
        event.preventDefault();
        console.log('klik')
        const data = new FormData();
        console.log(this.uploadInput.current.files[0]);
        console.log(this.uploadInput.current.files.length);
        data.append('file', this.uploadInput.current.files[0]);
         

        fetch('http://172.20.10.7:5000/upload', {
            method: 'POST',
            body: data, 
          }).then((response) => {
            console.log(response)
          });
        }

        readFile = (file) => {
            
        }


    render() {
        const { classes } = this.props;
            return (
                <div>
                <input
                        type="file"
                        ref={this.uploadInput}
                        onChange={this.handleImageUpload}
                        accept="image/*"
                        className={classes.input}
                        id='contained-button-file'
                        
                    />
                <label htmlFor='contained-button-file'>
                <Button  
                variant="contained" 
                component='span'
                className={classes.button}
                size='large'
                color="primary"
                disableRipple={true}
                >
                Upload
                <CloudUploadIcon className={classes.rightIcon} />
              </Button>
              </label>
              </div>
              );
    }
}

export default withStyles(styles)(Upload);