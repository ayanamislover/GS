const video = document.getElementById('qr-video');
const canvasElement = document.getElementById('qr-canvas');
const canvas = canvasElement.getContext('2d');
const btnScanQR = document.getElementById('btn-scan-qr');
const imageInput = document.getElementById('image-input');
const imageCanvasElement = document.getElementById('image-canvas');
const imageCanvas = imageCanvasElement.getContext('2d');

// the location of exeter
const targetLocation = {
    latitude: 50.7184, // The latitude of Exeter
    longitude: -3.5339, // the longitude of exeter
    radius: 5000 // 用户需要在这个半径范围内（单位：米）
};

// 检查用户位置是否在目标位置的指定半径内
function isInTargetLocation(userLat, userLong, targetLat, targetLong, radius) {
    const earthRadius = 6371e3; // 地球半径，单位：米
    const lat1 = userLat * Math.PI / 180;
    const lat2 = targetLat * Math.PI / 180;
    const deltaLat = (targetLat - userLat) * Math.PI / 180;
    const deltaLong = (targetLong - userLong) * Math.PI / 180;

    const a = Math.sin(deltaLat / 2) * Math.sin(deltaLat / 2) +
              Math.cos(lat1) * Math.cos(lat2) *
              Math.sin(deltaLong / 2) * Math.sin(deltaLong / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    const distance = earthRadius * c; // 最终结果，单位：米

    return distance <= radius;
}

btnScanQR.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
    .then(function(stream) {
        video.srcObject = stream;
        video.setAttribute('playsinline', true);
        video.play();
        btnScanQR.style.display = 'none';
        canvasElement.style.display = 'block';
        requestAnimationFrame(tick);
    })
    .catch(err => {
        console.error("Error accessing the camera", err);
    });
});

function tick() {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
        canvasElement.hidden = false;
        canvasElement.height = video.videoHeight;
        canvasElement.width = video.videoWidth;
        canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
        var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
        var code = jsQR(imageData.data, imageData.width, imageData.height, {
            inversionAttempts: "dontInvert",
        });
        if (code) {
            // 获取用户当前位置
            navigator.geolocation.getCurrentPosition(position => {
                const userLat = position.coords.latitude;
                const userLong = position.coords.longitude;

                // 检查用户是否在目标位置周围
                if (isInTargetLocation(userLat, userLong, targetLocation.latitude, targetLocation.longitude, targetLocation.radius)) {
                    // 用户在目标位置周围，允许跳转
                    window.location.href = code.data;
                } else {
                    // 用户不在目标位置周围，显示警告
                    alert("You are not in the required location to access this URL.");
                    video.srcObject.getTracks().forEach(track => track.stop());
                    canvasElement.style.display = 'none';
                    btnScanQR.style.display = 'block';
                }
            }, () => {
                // 无法获取位置信息
                alert("Unable to retrieve your location.");
            });
        } else {
            requestAnimationFrame(tick);
        }
    } else {
        requestAnimationFrame(tick);
    }
}

imageInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) {
        return;
    }
    const reader = new FileReader();
    reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
            imageCanvasElement.width = img.width;
            imageCanvasElement.height = img.height;
            imageCanvas.drawImage(img, 0, 0);
            const imageData = imageCanvas.getImageData(0, 0, img.width, img.height);
            const code = jsQR(imageData.data, imageData.width, imageData.height);
            if (code) {
                // 类似地，添加位置检查逻辑
                navigator.geolocation.getCurrentPosition(position => {
                    const userLat = position.coords.latitude;
                    const userLong = position.coords.longitude;
                    if (isInTargetLocation(userLat, userLong, targetLocation.latitude, targetLocation.longitude, targetLocation.radius)) {
                        window.location.href = code.data;
                    } else {
                        alert("You are not in the required location to access this URL.");
                    }
                }, () => {
                    alert("Unable to retrieve your location.");
                });
            } else {
                alert("No QR code found.");
            }
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
});