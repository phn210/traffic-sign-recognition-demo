import React from "react";
import { AppBar, Toolbar } from "@material-ui/core";
import { Container, Grid, CssBaseline } from "@material-ui/core";
import { Card, CardContent, CardMedia, CardActions } from "@material-ui/core";
import { Button } from "@material-ui/core";
import { Input, InputLabel, Select, MenuItem } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { PhotoCamera } from '@material-ui/icons';
import useStyles from "./styles";

const App = () => {
    const classes = useStyles();
    const [prediction1, setPrediction1] = React.useState('');
    const [prediction2, setPrediction2] = React.useState('');
    const [prediction3, setPrediction3] = React.useState('');
    const [img1, setImg1] = React.useState('');
    const [img2, setImg2] = React.useState('./upload.png');
    const [img3, setImg3] = React.useState('./upload.png');
    const [imgData1, setImgData1] = React.useState('./upload.png');
    const [imgData2, setImgData2] = React.useState('./upload.png');
    const [imgData3, setImgData3] = React.useState('./upload.png');
    const [result1, setResult1]  = React.useState('Result will be shown here');
    const [result2, setResult2]  = React.useState('Result will be shown here');
    const [result3, setResult3]  = React.useState('Result will be shown here');


    const handleChange1 = (event) => {
        setPrediction1(event.target.value);
    };

    const handleChange2 = (event) => {
        setPrediction2(event.target.value);
    };

    const handleChange3 = (event) => {
        setPrediction3(event.target.value);
    };

    const handleUpload1 = async (event) => {
        let formData = new FormData();
        var files = event.target.files;
        formData.append('file', event.target.files[0]);
        formData.append('method', prediction1);

        setImg1(files[0]);
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            setImgData1(reader.result);
        });
        reader.readAsDataURL(files[0]);

        const response = await fetch("/predict/img", {
            method:'POST',
            headers: {
                'enctype': 'multipart/form-data'
            },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            if(data.hasOwnProperty('upload_result')) {
                if(data['upload_result'] == 1) {
                    if(data['method'] != 0) {
                        if(data['class_name'] != '') setResult1(data['class_name'].toString());
                        else setResult1('No signs detected!')
                    } else setResult1('Successfully uploaded but no method chosen!');
                } else setResult1('Failed to upload file! Please upload again.');
            } else setResult1('Some error occurred! Please upload again.');
        }
        
    };

    const handleUpload2 = async (event) => {
        let formData = new FormData();
        var files = event.target.files;
        formData.append('file', event.target.files[0]);
        formData.append('method', prediction2);

        setImg1(files[0]);
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            setImgData2(reader.result);
        });
        reader.readAsDataURL(files[0]);

        const response = await fetch("/predict/img", {
            method:'POST',
            headers: {
                'enctype': 'multipart/form-data'
            },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            if(data.hasOwnProperty('upload_result')) {
                if(data['upload_result'] == 1) {
                    if(data['method'] != 0) {
                        if(data['class_name'] != '') setResult2(data['class_name'].toString());
                        else setResult2('No signs detected!')
                    } else setResult2('Successfully uploaded but no method chosen!');
                } else setResult2('Failed to upload file! Please upload again.');
            } else setResult2('Some error occurred! Please upload again.');
        }
    };

    const handleUpload3 = async (event) => {
        let formData = new FormData();
        var files = event.target.files;
        formData.append('file', event.target.files[0]);
        formData.append('method', prediction3);

        setImg1(files[0]);
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            setImgData3(reader.result);
        });
        reader.readAsDataURL(files[0]);

        const response = await fetch("/predict/img", {
            method:'POST',
            headers: {
                'enctype': 'multipart/form-data'
            },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            if(data.hasOwnProperty('upload_result')) {
                if(data['upload_result'] == 1) {
                    if(data['method'] != 0) {
                        if(data['class_name'] != '') setResult3(data['class_name'].toString());
                        else setResult3('No signs detected!')
                    } else setResult3('Successfully uploaded but no method chosen!');
                } else setResult3('Failed to upload file! Please upload again.');
            } else setResult3('Some error occurred! Please upload again.');
        }
    };

    return (
        <>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                    {/* <CameraIcon className={classes.icon} /> */}
                    <Typography variant="h6" color="inherit" noWrap>
                        Computer Vision - IT4350
                    </Typography>
                </Toolbar>
            </AppBar>
            <main>
                <div>
                    <Container maxWidth="md" style={{padding: "2rem 0"}}>
                        <Typography variant="h3" align="center" color="textPrimary" gutterBottom>
                            Traffic Signs Recognition
                        </Typography>
                        <Typography variant="h6" align="center" color="textSecondary" gutterBottom>
                            Your file will be process after successfully uploaded
                        </Typography>
                    </Container>
                </div>
                <Container className={classes.cardGrid} maxWidth="md">
                    <Grid container spacing={3}>
                        <Grid item xs={4}>
                            <Card className={classes.card} style={{padding:"0.5rem"}}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image={imgData1}
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography align="center" style={{minHeight:"3rem"}}>
                                        {result1}
                                    </Typography>
                                </CardContent>
                                <CardActions className={classes.cardActions}>
                                    <Button
                                        variant="contained"
                                        component="label"
                                        color="primary"
                                        >
                                        Upload File
                                        <input
                                            type="file"
                                            name="file"
                                            hidden
                                            onChange={handleUpload1}
                                            multiple={false}
                                            value=''
                                        />
                                        </Button>
                                    <InputLabel id="img-method-select-1-label">Method</InputLabel>
                                    <Select
                                        labelId="img-method-select-1-label"
                                        id="img-method-select-1"
                                        value={prediction1}
                                        onChange={handleChange1}
                                        label="Prediction Method"
                                    >
                                        <MenuItem value="">
                                            <em>None</em>
                                        </MenuItem>
                                        <MenuItem value={'CNN'}>CNN</MenuItem>
                                        <MenuItem value={'VGG16'}>VGG16</MenuItem>
                                        <MenuItem value={'YOLO'}>YOLO</MenuItem>
                                    </Select>
                                </CardActions>
                            </Card>
                        </Grid>
                        <Grid item xs={4}>
                            <Card className={classes.card} style={{padding:"0.5rem"}}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image={imgData2}
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography align="center" style={{minHeight:"3rem"}}>
                                        {result2}
                                    </Typography>
                                </CardContent>
                                <CardActions className={classes.cardActions}>
                                    <Button
                                        variant="contained"
                                        component="label"
                                        color="primary"
                                        >
                                        Upload File
                                        <input
                                            type="file"
                                            name="file"
                                            hidden
                                            onChange={handleUpload2}
                                            multiple={false}
                                            value=''
                                        />
                                        </Button>
                                    <InputLabel id="img-method-select-2-label">Method</InputLabel>
                                    <Select
                                        labelId="img-method-select-2-label"
                                        id="img-method-select-2"
                                        value={prediction2}
                                        onChange={handleChange2}
                                        label="Prediction Method"
                                    >
                                        <MenuItem value="">
                                            <em>None</em>
                                        </MenuItem>
                                        <MenuItem value={'CNN'}>CNN</MenuItem>
                                        <MenuItem value={'VGG16'}>VGG16</MenuItem>
                                        <MenuItem value={'YOLO'}>YOLO</MenuItem>
                                    </Select>
                                </CardActions>
                            </Card>
                        </Grid>
                        <Grid item xs={4}>
                            <Card className={classes.card} style={{padding:"0.5rem"}}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image={imgData3}
                                    title="Test"
                                />
                                <CardContent>
                                    <Typography align="center" style={{minHeight:"3rem"}}>
                                        {result3}
                                    </Typography>
                                </CardContent>
                                <CardActions className={classes.cardActions}>
                                    <Button
                                        variant="contained"
                                        component="label"
                                        color="primary"
                                        >
                                        Upload File
                                        <input
                                            type="file"
                                            name="file"
                                            hidden
                                            onChange={handleUpload3}
                                            multiple={false}
                                            value=''
                                        />
                                        </Button>
                                    <InputLabel id="img-method-select-3-label">Method</InputLabel>
                                    <Select
                                        labelId="img-method-select-3-label"
                                        id="img-method-select-3"
                                        value={prediction3}
                                        onChange={handleChange3}
                                        label="Prediction Method"
                                    >
                                        <MenuItem value="">
                                            <em>None</em>
                                        </MenuItem>
                                        <MenuItem value={'CNN'}>CNN</MenuItem>
                                        <MenuItem value={'VGG16'}>VGG16</MenuItem>
                                        <MenuItem value={'YOLO'}>YOLO</MenuItem>
                                    </Select>
                                </CardActions>
                            </Card>
                        </Grid>
                    </Grid>
                    
                </Container>
            </main>
        </>
    );
}

export default App;