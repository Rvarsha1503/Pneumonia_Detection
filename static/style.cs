body {
    font-family: Arial, sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
   
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.image-preview {
    max-width: 5rem; /* Set the maximum width */
    max-height: 5rem; /* Set the maximum height */
    width: auto; /* Allow the width to adjust according to the aspect ratio */
    height: auto; /* Allow the height to adjust according to the aspect ratio */
    border-radius: 10px; /* Add border-radius if desired */
}


.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    text-align: center;
}

h1 {
    font-size: 2em;
    margin-bottom: 20px;
}

.image-container img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
    border-radius: 10px;
}

.btn-container {
    margin-top: 20px;
}

.btn {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #0600b3;
}

.predicted-class {
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 20px;
}
#helpBot {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 320px;
    background-color: rgba(255,255,255, 0.75);
    border: 1px solid #ced4da;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: none;
    flex-direction: column;
    justify-content: space-between;
    z-index: 1000;
    color :black;
}

#helpBotHeader {
    background-color: rgba(0,0,0, 0.9);
    color: white;
    padding: 10px;
    border-radius: 10px 10px 0 0;
    cursor: pointer;
}

#helpBotBody {
    padding: 10px;
    max-height: 200px;
    overflow-y: auto;
}

#helpBotFooter {
    padding: 10px;
    border-top: 1px solid #ced4da;
}

#helpBotFooter input {
    width: calc(100% - 20px);
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 5px;
    outline: none;
}

#helpBotFooter input:focus {
    border-color: black;
}

#helpBotToggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color:black ;
    color: white;
    border: white;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    font-size: 24px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    z-index: 1001;
}
#helpBotToggle i {
        font-size: 20px;
}
.example-keywords {
    margin-top: 10px;
    font-size: 0.9em;
}

.example-keywords a {
    display: inline-block;
    padding: 5px 10px;
    margin-right: 10px;
    background-color: rgb(12, 10, 74);
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    margin-bottom:3px;
}

.example-keywords a:hover {
    background-color: black;
}
.user-message {
    background-color: rgb(12, 10, 74) ;
    border-radius: 10px;
    padding: 10px;
    margin-left: 15px ;
    color :white;
    margin-top:5px;
}

.bot-message {
    background-color: #007bff; /* Primary color for bot message */
    color: #fff;
    border-radius: 10px;
    padding: 10px;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    width :80%;
}

/* Bot message prefix */
.bot-message::before {
    content:  <i style = "color :black" class=" fa prefix fa-solid fa-robot "></i>; /* Unicode for the robot head icon */
    font-family: "Font Awesome 5 Regular"; /* Font family for Font Awesome Regular icons */
    font-weight: 900; /* Font weight for bold */
    margin-right: 5px;
}