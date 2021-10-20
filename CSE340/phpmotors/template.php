<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Gemunu+Libre&display=swap" rel="stylesheet">
    <title>PHP Motors Template</title>
</head>

<body>
    <div class="wrapper">
        <header>
            <?php require_once $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/modules/header.php'; ?>
        </header>

        <nav>
       <?php require $_SERVER['DOCUMENT_ROOT']. '/phpmotors/modules/nav.php'; ?>
    </nav>
        </nav>

        <main>
            <h1>Content Here</h1>
        </main>

        <footer>
            <?php require_once $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/modules/footer.php'; ?>
        </footer>
    </div>
</body>

</html>