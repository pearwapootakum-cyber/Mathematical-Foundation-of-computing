import matplotlib.pyplot as plt
import folium

def plot_graph(df, user_pos):
    plt.figure(figsize=(8,8))

    plt.scatter(df["longitude"], df["latitude"], label="WiFi AP")
    plt.scatter(user_pos[0], user_pos[1], color="red", label="User")

    plt.legend()
    plt.title("WiFi Multilateration")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.show()


def create_map(df, user_pos):
    m = folium.Map(location=[user_pos[1], user_pos[0]], zoom_start=18)

    # user marker
    folium.Marker(
        [user_pos[1], user_pos[0]],
        popup="User Position",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # wifi markers
    for _, row in df.iterrows():
        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=row["ssid"]
        ).add_to(m)

    m.save("wifi_map.html")
    print("Map saved as wifi_map.html")
