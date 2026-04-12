window.onload = function () {
  google.accounts.id.initialize({
    client_id: "1003730491521-2ln1uac6mrr7m1e4g73g9vni2al14ulg.apps.googleusercontent.com",
    callback: handleCredentialResponse // This will log your info
  });
  google.accounts.id.renderButton(
    document.getElementById("buttonDiv"),
    { theme: "outline", size: "large" }
  );
}

async function handleCredentialResponse(response) {
   console.log("Encoded JWT ID token: " + response.credential);

   response = await fetch("/login", 
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"token": response.credential})
        }
   )

   response_obj = await response.json()

   document.getElementById("buttonDiv").innerHTML = response_obj["email"]
}