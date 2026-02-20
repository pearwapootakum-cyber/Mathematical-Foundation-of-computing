<script>
navigator.geolocation.getCurrentPosition(function(pos) {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;

    fetch(`/get_location?lat=${lat}&lon=${lon}`)
})
</script>
