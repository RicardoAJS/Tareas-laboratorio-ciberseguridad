#Ricardo Adhiel Jacobo Sanjuan

"Este programa sirve para eliminar archivos de la carpeta descargas que ya fueron utilizados y olvide borrar"

$ciclo = 1

function ArchivoBorrado{

 param ([string]$Archivo2)

 $Archivo2 = $Archivo

 Write-Host "El archivo $Archivo2 fue borrado exitosamente"
 }


 While ($ciclo -lt 2){

  "Escribe el nombre del archivo que deseas eliminar no olvides su extensión"

   $Archivo = Read-Host "Introduce el nombre del archivo que se borrara"

   "Estas seguro que quieres borrar el archivo?"

   
   remove-item C:\Users\ur\Downloads\$Archivo
    ArchivoBorrado





   "Si deseas eliminar otro archivo escribe 1 , si no presiona 2 para salir"

   $ciclo2 = Read-Host "Seleccione una opcion"

   if($ciclo2 -lt 2){$ciclo = 1}

   else{$ciclo = 2}

  
}