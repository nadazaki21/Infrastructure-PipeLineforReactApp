// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {apiKey: "AIzaSyBaJ7ba5SrBFQRHVf_ELGpbO64EtIPr1AY",

authDomain: "react-chat-afcdf.firebaseapp.com",

projectId: "react-chat-afcdf",

storageBucket: "react-chat-afcdf.appspot.com",

messagingSenderId: "927361667600",

appId: "1:927361667600:web:cdb7d196d9e42e53ddb095"

  
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

export { auth, db, storage };
