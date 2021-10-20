<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Gemunu+Libre&display=swap" rel="stylesheet">
    <link rel="stylesheet" href='css/styles.css' media='screen'>
    <title>PHP Motors | Web Backend Development I</title>
</head>

<body>
    <div class="wrapper">
        <header>
            <?php require_once $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/modules/header.php'; ?>
        </header>

        <nav>
             <?php require $_SERVER['DOCUMENT_ROOT']. '/phpmotors/modules/nav.php'; ?>
        </nav>

        <main>
            <h1>Welcome to PHP Motors!</h1>

            <section class='car'>
                <div class="car-container">
                    <img class='car-img' src="images/delorean.jpg" alt="">

                    <div class="car-info">
                        <h2>DMC Delorean</h2>
                        <span>3 cup holders</span>
                        <span>Superman doors</span>
                        <span>Fuzzy dice!</span>
                    </div>

                    <img class='car-own' src="images/site/own_today.png" alt="Own Today Logo">
                </div>
            </section>

            <div class="features">
                <section class='info'>
                    <h2>DMC Delorean Reviews</h2>
                    <ul>
                        <li>"So fast it's almost like traveling in time." (4/5)</li>
                        <li>"Coolest ride on the road." (4/5)</li>
                        <li>"I'm feeling Marty McFly!." (5/5)</li>
                        <li>"The most futuristic ride of our day." (4/5)</li>
                        <li>"80's livin and love it." (5/5)</li>
                    </ul>
                </section>

                <section class='upgrades'>
                    <h2>Delorean Upgrades</h2>
                    <div class="upgrades-container">
                        <div class="upgrades-img">
                            <img src="images/upgrades/flux-cap.png" alt="Delorean upgrades">
                        </div>

                        <p>Flux Capacitor</p>
                    </div>
                    <div class="upgrades-container">
                        <div class="upgrades-img">
                            <img src="images/upgrades/flame.jpg" alt="Flux Capacitor">
                        </div>

                        <p>Flame Decals</p>
                    </div>
                    <div class="upgrades-container">
                        <div class="upgrades-img">
                            <img src="images/upgrades/bumper_sticker.jpg" alt="Flame Decals">
                        </div>

                        <p>Bumper Stickers</p>
                    </div>
                    <div class="upgrades-container">
                        <div class="upgrades-img">
                            <img src="images/upgrades/hub-cap.jpg" alt="Bumper Sticker">
                        </div>

                        <p>Hub Caps</p>
                    </div>
                </section>
            </div>
        </main>

        <footer>
            <?php require_once $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/modules/footer.php'; ?>
        </footer>
    </div>
</body>

</html>