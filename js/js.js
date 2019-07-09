
$.ajax({
            type: "GET",
            url: "/get_feeds",
        }).done(function (data) {
            var container=document.getElementsByClassName("container")[0];

            var feeds = JSON.parse(data);
            console.log(feeds)
            feeds.forEach(element => {
                var div = document.createElement("div");
                div.className="little-link";
                div.innerHTML=`<h3>${element.title}</h3><a>${element.link}</a>`
                container.appendChild(div);
            });
        });
        