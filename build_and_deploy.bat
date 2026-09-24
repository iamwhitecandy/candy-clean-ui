@echo off
chcp 65001 > nul
echo [Candy Clean UI] Сборка мода...
python "C:\Users\User\Desktop\candy-clean-ui\build_mod.py"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Ошибка сборки!
    pause
    exit /b %ERRORLEVEL%
)

echo [Candy Clean UI] Копирование в клиент, лаунчсервер и сборки...
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\AppData\Roaming\ServerCandy\updates\Fabric-1.21.1\mods\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\Desktop\gravit-fabric-1.21.1\launchserver\updates\Fabric-1.21.1\mods\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\Desktop\gravit-fabric-1.21.1\launchserver\updates\Test-1.21.1\mods\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\Desktop\сборка 2\1_Клиент\mods\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\Desktop\сборка 2\3_Моды_по_категориям\14_Интерфейс_и_Красота\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\Desktop\сборка\mods\candy-clean-ui-1.0.0.jar"
copy /Y "C:\Users\User\Desktop\candy-clean-ui\build\libs\candy-clean-ui-1.0.0.jar" "C:\Users\User\AppData\Roaming\.minecraft\mods\candy-clean-ui-1.0.0.jar"

echo [SUCCESS] Мод успешно собран и разложен по всем папкам!
pause
