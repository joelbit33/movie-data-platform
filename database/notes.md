# Connecting to Render's PostgreSQL Instance Using DBeaver

This guide outlines the steps to connect to a PostgreSQL database hosted on Render using DBeaver, a popular database management tool.

## Important Note:
The PostgreSQL database instance on Render is configured to be taken down after 90 days. However, all scripts used for setting up and managing the database are saved. This ensures that setting up a new instance and restoring the database can be done quickly by re-running the entire setup process.

## Connection Steps:

1. **Open DBeaver** and navigate to the **Database** menu, then select **New Database Connection**.

2. Choose **PostgreSQL** as the database type and proceed to the connection settings form.

3. In the **Render Dashboard**, locate your PostgreSQL database instance. Render provides an external URL for your database, which includes all necessary connection details.

4. **Extract the following details** from the Render-provided external URL:
   - Hostname
   - Port
   - Database Name (dbname)
   - Username
   - Password

   The URL from Render typically follows this format: `postgresql://username:password@hostname:port/dbname`. Extract each component accordingly.

5. **Enter the extracted details** into the corresponding fields in DBeaver's connection settings form:
   - **Host**: The `hostname` from the URL.
   - **Port**: Typically `5432`, unless specified differently in the URL.
   - **Database/Schema**: The `dbname` part of the URL.
   - **User Name**: Your database `username`.
   - **Password**: The `password` for database access.

6. After filling in the connection details, click **Test Connection** in DBeaver to ensure everything is set up correctly. If the test is successful, you can finish the setup and start working with your database.

## Note on Connection URL:

DBeaver may not correctly parse the entire external URL provided by Render due to its format. It's recommended to manually extract and input the connection details as described above.

## Re-establishing Connection After 90 Days:

Since the Render instance will be taken down after 90 days, you'll need to set up a new instance on Render and update your connection details in DBeaver accordingly. Keeping a backup of your scripts and data will simplify this process, allowing for quick restoration of your database environment.
