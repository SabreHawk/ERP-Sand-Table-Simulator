import Repository
import RawMaterial
import ERPSystem
import DatabaseManager

if __name__ == '__main__':
    temp_system = DatabaseManager.DatabaseManager()
    temp_system.init_database_raw_material_info()
    temp_system.testQuery()