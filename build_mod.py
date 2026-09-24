import glob
import os
import subprocess
import zipfile
import shutil

base = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(base, "src", "main", "java")
res_dir = os.path.join(base, "src", "main", "resources")
build_dir = os.path.join(base, "build")
classes_dir = os.path.join(build_dir, "classes")
libs_out = os.path.join(build_dir, "libs")

if os.path.exists(classes_dir):
    shutil.rmtree(classes_dir)
os.makedirs(classes_dir, exist_ok=True)
os.makedirs(libs_out, exist_ok=True)

# Find all java source files
java_files = []
for root, _, files in os.walk(src_dir):
    for f in files:
        if f.endswith(".java"):
            java_files.append(os.path.join(root, f))

print(f"Compiling {len(java_files)} Java files...")

# Classpath
libs = glob.glob(r"C:\Users\User\AppData\Roaming\ServerCandy\updates\Fabric-1.21.1\libraries\**\*.jar", recursive=True)
mc = r"C:\Users\User\AppData\Roaming\ServerCandy\updates\Fabric-1.21.1\.fabric\remappedJars\minecraft-1.21.1-0.19.3\client-intermediary.jar"
fabric_api = r"C:\Users\User\AppData\Roaming\ServerCandy\updates\Fabric-1.21.1\mods\fabric-api-0.116.15+1.21.1.jar"

cp_list = [mc, fabric_api] + libs
cp = ";".join(cp_list)

cmd = [
    "javac",
    "-cp", cp,
    "-d", classes_dir,
    "-proc:none",
    "-encoding", "UTF-8",
    "--release", "21"
] + java_files

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("Compilation FAILED!")
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    exit(1)
else:
    print("Compilation SUCCESSFUL!")

# Package into JAR
jar_path = os.path.join(libs_out, "candy-clean-ui-1.0.0.jar")
if os.path.exists(jar_path):
    os.remove(jar_path)

with zipfile.ZipFile(jar_path, "w", zipfile.ZIP_DEFLATED) as zf:
    # 1. Add compiled classes
    for root, _, files in os.walk(classes_dir):
        for f in files:
            full_path = os.path.join(root, f)
            arcname = os.path.relpath(full_path, classes_dir)
            zf.write(full_path, arcname)
    # 2. Add resources
    for root, _, files in os.walk(res_dir):
        for f in files:
            full_path = os.path.join(root, f)
            arcname = os.path.relpath(full_path, res_dir)
            zf.write(full_path, arcname)

print(f"JAR created: {jar_path} (size: {os.path.getsize(jar_path)} bytes)")
