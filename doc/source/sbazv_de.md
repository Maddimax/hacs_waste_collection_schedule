# Südbrandenburgischer Abfallzweckverband

Support for schedules provided by [https://www.sbazv.de/](https://www.sbazv.de/).


## Configure via UI

* Go to https://www.sbazv.de/entsorgungstermine/restmuell-papier-gelbesaecke-laubsaecke-weihnachtsbaeume/
* Fill in the address
* Click "URL in die Zwischenablage kopieren"
* Copy it into the "url" field

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: sbazv_de
      args:
        url: URL_COPIED_FROM_WEBSITE
```

### Configuration Variables

**url**  
*(string) (required)*

## Example

```yaml
waste_collection_schedule:
  sources:
    - name: sbazv_de
      args:
        urL: https://fahrzeuge.sbazv.de/WasteManagementSuedbrandenburg/WasteManagementServiceServlet?ApplicationName=Calendar&SubmitAction=sync&StandortID=1369739001&AboID=10760&Fra=P;R;WB;L;GS
```

